def local(rec, sat):
    """
    Calculates the azimuth, zenith angle, and slant distance between a receiver and a satellite.
    
    Args:
        rec (np.array): Receiver coordinates [x, y, z] in meters.
        sat (np.array): Satellite coordinates [x, y, z] in meters.
    
    Returns:
        az (float): Azimuth angle in degrees.
        zen (float): Zenith angle in degrees.
        slantd (float): Slant distance between the receiver and satellite in kilometers.
    """
   
    # Convert receiver coordinates to latitude and longitude
    ellp = xyz2plh(rec)
    lat = ellp[0] #lat
    lon = ellp[1] #lon
    
    # Calculate vector difference between satellite and receiver positions
    delta_x = sat - rec
    
    # Rotation matrix
    A = np.array([[-np.sin(np.deg2rad(lat)) * np.cos(np.deg2rad(lon)), -np.sin(np.deg2rad(lon)), np.cos(np.deg2rad(lat)) * np.cos(np.deg2rad(lon))],
                  [-np.sin(np.deg2rad(lat)) * np.sin(np.deg2rad(lon)), np.cos(np.deg2rad(lon)), np.cos(np.deg2rad(lat)) * np.sin(np.deg2rad(lon))],
                  [np.cos(np.deg2rad(lat)), 0, np.sin(np.deg2rad(lat))]])
    
    # Transform the vector difference to the local coordinate system
    delta_x2 = np.dot(A.T, delta_x)
    
    # Extract the components of the transformed vector
    xe, ye, ze = delta_x2.ravel()
    
    # Calculate azimuth and zenith angle
    azmth = np.degrees(np.arctan2(ye, xe))
    zenith = np.degrees(np.arctan2(np.hypot(xe, ye), ze))
    
    # Calculate slant distance
    slantd = np.linalg.norm(delta_x2) * 1e-3  # kilometer
    
    # Calculate slant distance
    az = azmth % 360 if 0 < azmth < 360 else azmth % 360
    zen = zenith % 90 if zenith < 90 or -90 < zenith else zenith % 90 if zenith > 90 else zenith % -90
    
    return az, zen, slantd
