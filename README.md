# local (rec, sat)

**Function Description:**
The `local` function calculates the azimuth angle, zenith angle, and slant distance between a receiver and a satellite. The function computes these angles and distance in the local coordinate system defined by the latitude and longitude of the receiver.

<img width="700" alt="image" src="https://github.com/sudeyaprak/local/assets/119863892/76e8839c-8ede-492a-8c59-7f99b66a82b2">

**Arguments:**
1. `rec` (np.array): A NumPy array representing the receiver coordinates `[x, y, z]` in meters. The receiver coordinates are specified in the Earth-Centered, Earth-Fixed (ECEF) coordinate system.
2. `sat` (np.array): A NumPy array representing the satellite coordinates `[x, y, z]` in meters. The satellite coordinates are also specified in the ECEF coordinate system.

**Returns:**
The function returns three values as a tuple:
1. `az` (float): The azimuth angle in degrees, measured clockwise from the North direction.
2. `zen` (float): The zenith angle in degrees, representing the angle between the satellite and the vertical direction directly above the receiver.
3. `slantd` (float): The slant distance between the receiver and the satellite in kilometers.

**Function Logic:**
1. The function begins by converting the receiver coordinates (`rec`) from ECEF to latitude and longitude using the `xyz2plh` function. The resulting latitude and longitude are extracted from the `ellp` array.
2. The vector difference (`delta_x`) between the satellite and receiver positions is calculated by subtracting the receiver coordinates (`rec`) from the satellite coordinates (`sat`).
3. The rotation matrix `A` is constructed based on the latitude and longitude of the receiver. This matrix is used to transform the vector difference `delta_x` into the local coordinate system.
4. The transformed vector difference (`delta_x2`) is obtained by multiplying the transpose of the rotation matrix (`A.T`) with the vector difference `delta_x`.
5. The components `xe`, `ye`, and `ze` are extracted from the transformed vector difference `delta_x2`.
6. The azimuth angle (`azmth`) and zenith angle (`zenith`) are computed using trigonometric functions based on the components `xe` and `ye`. The `np.arctan2` function is used to handle the quadrant ambiguity in angle calculations.
7. The slant distance (`slantd`) is calculated as the Euclidean norm of the transformed vector difference `delta_x2` divided by 1000 to convert it from meters to kilometers.
8. The azimuth angle `az` is adjusted to be between 0 and 360 degrees by taking the modulo 360.
9. The zenith angle `zen` is adjusted to be between 0 and 90 degrees by taking the modulo 90. If the zenith angle is outside the range of 0 to 90 degrees, it is adjusted to be between 0 and 90 or between 0 and -90 degrees.
10. The function returns the azimuth angle `az`, zenith angle `zen`, and slant distance `slantd` as a tuple.

**Note:**
The function assumes that the `xyz2plh` function correctly converts ECEF coordinates to latitude and longitude. Additionally, the accuracy of the azimuth, zenith angle, and slant distance calculations depends on the accuracy of the provided receiver and satellite coordinates. It's essential to ensure the coordinates are accurate and consistent for reliable results.
