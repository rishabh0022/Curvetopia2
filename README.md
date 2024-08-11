# Curvetopia

# SVG to CSV Converter


## Overview

This script extracts coordinates from an SVG file and saves them to a CSV file.

## Dependencies

- `csv`: For writing CSV files.
- `xml.etree.ElementTree` (ET): For parsing XML data from SVG files.
- `os`: For file path operations.

## File Paths

- **`svg_file_path`**: Path to the input SVG file.
- **`csv_file_path`**: Path to the output CSV file.

## Functions

- **`parse_svg(svg_file)`**: Parses the SVG file and returns the XML root element.
- **`extract_paths(root)`**: Extracts path data (`d` attribute) from SVG paths.
- **`extract_circles(root)`**: Extracts circle center coordinates (`cx`, `cy`) from SVG circles.
- **`extract_rects(root)`**: Extracts rectangle corner coordinates from SVG rectangles.

## Process

1. **Parse the SVG file**: `parse_svg()`.
2. **Extract Data**:
   - Paths: `extract_paths()`.
   - Circles: `extract_circles()`.
   - Rectangles: `extract_rects()`.
3. **Save Coordinates to CSV**:
   - Write coordinates to CSV file using `csv.writer()`.

## Output

Coordinates are saved to `csv_file_path` in CSV format with columns `x` and `y`.

# Curvetopia2

# Shape Regularization Code 
https://colab.research.google.com/drive/1-UhLD_altVKm40WxTGB1qzYx_d9Zdnrj#scrollTo=bRTqeV0GFIac (collab link)

## Functions

- **`read_csv(csv_path)`**: Reads shape data from a CSV file.
- **`plot(paths_XYs, colours)`**: Plots multiple shapes.
- **`plot_shape(paths_XYs, colours)`**: Plots individual shapes.
- **`regularize_line(points)`**: Regularizes points into a line.
- **`regularize_ellipse(points)`**: Regularizes points into an ellipse.
- **`regularize_circle(points, max_width, max_height, scale_factor=0.9)`**: Regularizes points into a circle.
- **`regularize_rectangle(points, max_width, max_height, scale_factor=0.9)`**: Regularizes points into a rectangle.
- **`regularize_rounded_rectangle(points)`**: Regularizes points into a rounded rectangle.
- **`regularize_star(points)`**: Regularizes points into a star.
- **`regularize_arc(points)`**: Regularizes points into an arc.
- **`regularize_triangle(points)`**: Regularizes points into a triangle.
- **`regularize_polygon(points)`**: Regularizes points into a polygon.
- **`regularize_irregular(points, epsilon=0.1)`**: Simplifies irregular shapes.
- **`fit_circle(points)`**: Fits a circle to points.
- **`calculate_perimeter(hull)`**: Calculates perimeter of a convex hull.
- **`identify_shape(points)`**: Identifies the shape type.
- **`calculate_max_extents(points)`**: Calculates the bounding box dimensions.
- **`calculate_aspect_ratio(points)`**: Calculates aspect ratio of a shape.
- **`regularize_shape(points)`**: Regularizes shape based on type.

## Usage

1. Load shapes with `read_csv()`.
2. Visualize with `plot()`.
3. Regularize shapes using `regularize_shape()`.
4. Plot regularized shapes with `plot()`.




# Symmetry Analysis and Reflection in Python
https://colab.research.google.com/drive/1avp6mQBkVb_2uRguAOVLdydyOR2rVSQ8#scrollTo=naIFbm36E95q (Collab link)


## Overview

This script performs symmetry analysis on shapes extracted from a CSV file, visualizes the original and reflected shapes, and identifies the best symmetry axis for the given shapes.

## Libraries Used

- `google.colab.drive`: For mounting Google Drive to access data.
- `numpy`: For numerical operations.
- `scipy.spatial.ConvexHull`: For convex hull calculations (not used in this code).
- `matplotlib.pyplot`: For plotting.
- `cv2`: For OpenCV functions (not used in this code).
- `scipy.ndimage`: For image processing (not used in this code).
- `skimage.measure.EllipseModel`: For ellipse fitting (not used in this code).
- `scipy.optimize.least_squares`: For optimization (not used in this code).

## Functions

- **`read_csv(csv_path)`**: Reads coordinates from a CSV file and organizes them by shape and segment.
- **`rdp(points, epsilon)`**: Applies the Ramer-Douglas-Peucker (RDP) algorithm to simplify a curve.
- **`apply_rdp(path_XYs, epsilon=1.0)`**: Applies the RDP algorithm to each path in the dataset.
- **`reflect_points_across_vertical(points, x_line)`**: Reflects points across a vertical line.
- **`reflect_points_across_horizontal(points, y_line)`**: Reflects points across a horizontal line.
- **`reflect_points_across_line(points, line_point, line_direction)`**: Reflects points across a specified line.
- **`find_symmetry_and_reflect_1(path_XYs, symmetry_type)`**: Reflects paths based on symmetry type (vertical, horizontal, or diagonal).
- **`find_symmetry_and_reflect(path_XYs, symmetry_type)`**: Reflects paths across lines at various angles.
- **`plot_paths_with_symmetry(original_paths, reflected_paths, colours, symmetry_type)`**: Plots original and reflected paths with different colors.
- **`plot(path_XYs, colours)`**: Plots the given paths.
- **`calculate_alignment(original_paths, reflected_paths)`**: Calculates alignment score between original and reflected paths.
- **`find_best_symmetry_axis(original_paths)`**: Finds the best symmetry axis by evaluating various angles.
- **`plot_best_symmetry(original_paths, best_angle)`**: Plots paths with the best symmetry angle.

## Process

1. **Mount Google Drive**: Access CSV files from Google Drive.
2. **Read CSV**: Load coordinates from CSV files using `read_csv()`.
3. **Simplify Paths**: Apply RDP algorithm to simplify paths with `apply_rdp()`.
4. **Visualize Original and Reflected Paths**:
   - Plot original paths.
   - Reflect paths across vertical, horizontal, and diagonal lines using `find_symmetry_and_reflect_1()`.
   - Reflect paths at various angles using `find_symmetry_and_reflect()`.
   - Plot reflected paths alongside original paths with `plot_paths_with_symmetry()`.
5. **Evaluate Symmetry**:
   - Calculate alignment scores between original and reflected paths using `calculate_alignment()`.
   - Identify the best symmetry angle using `find_best_symmetry_axis()`.
6. **Plot Best Symmetry**: Visualize paths with the best symmetry angle using `plot_best_symmetry()`.

## Execution

The script processes a given CSV file, performs symmetry analysis, and visualizes the results. Modify `csv_path` to test different datasets.



# Occlusion Analysis and Visualization
https://colab.research.google.com/drive/1Nh3WMH9t6w-4JDIAnsAJ1wLxWCly-cmz


## Overview

This notebook processes paths from CSV files, simplifies them, fills occlusions, and visualizes the results. It also converts paths to SVG format for further analysis.

## Libraries Used

- `google.colab.drive`: For mounting Google Drive to access data.
- `numpy`: For numerical operations.
- `scipy.spatial.ConvexHull`: For computing convex hulls.
- `matplotlib.pyplot`: For plotting.
- `cv2`: For OpenCV functions (not used in this code).
- `scipy.ndimage`: For image processing (not used in this code).
- `skimage.measure.EllipseModel`: For ellipse fitting (not used in this code).
- `scipy.optimize.least_squares`: For optimization (not used in this code).
- `scipy.interpolate.splprep, splev`: For spline interpolation.
- `shapely.geometry`: For geometric operations and polygon handling.
- `shapely.ops.unary_union`: For unifying multiple polygons.
- `shapely.validation.make_valid`: For validating polygons.
- `rdp`: For Ramer-Douglas-Peucker (RDP) algorithm for curve simplification.
- `svgwrite`: For creating SVG files.
- `cairosvg`: For converting SVG to PNG.

## Functions

- **`read_csv(csv_path)`**: Reads coordinates from a CSV file and organizes them by shape and segment.
- **`polylines2svg(paths_XYs, svg_path, colours)`**: Converts a list of paths into an SVG file and also generates a PNG version.
- **`rdp_simplify(path_XYs, epsilon=1.0)`**: Simplifies paths using the RDP algorithm to reduce the number of points while preserving shape.
- **`fill_occlusions(paths_XYs)`**: Fills gaps in shapes by creating convex hulls around them.
- **`fit_bezier_curve(points, num_points=100)`**: Fits a Bezier curve to a set of points for smoother representation.
- **`plot_curves(paths_XYs, colours)`**: Plots curves, filling and smoothing them as needed.
- **`analyze_connectivity(paths_XYs)`**: Analyzes the connectivity of paths, checking if they form a single connected area.
- **`process_csv_and_fill_occlusions(input_csv, colours)`**: Reads CSV data, simplifies paths, fills occlusions, and checks connectivity.

## Process

1. **Mount Google Drive**: Access CSV files from Google Drive.
2. **Read CSV**: Load coordinates from CSV files using `read_csv()`.
3. **Simplify Paths**: Apply RDP algorithm to simplify paths with `rdp_simplify()`.
4. **Visualize Curves**: Plot the simplified curves with `plot_curves()`.
5. **Fill Occlusions**: Use `fill_occlusions()` to fill gaps in shapes and plot the results.
6. **Check Connectivity**: Analyze connectivity before and after filling occlusions using `analyze_connectivity()`.
7. **Convert to SVG**: Convert simplified paths to SVG and PNG formats using `polylines2svg()`.

## Execution

- **Process 1**: 
  - Read and process the CSV file `occlusion1.csv`.
  - Simplify and fill occlusions.
  - Visualize and save results in SVG format.

- **Process 2**: 
  - Repeat the process for `occlusion2.csv`.

Modify `input_csv` and `colours` variables as needed to test different datasets and visualizations.



# Fragments Analysis and Visualization
https://colab.research.google.com/drive/1g-cSz3BDMs1gi9xEk1eD7-uJMpXroasl

## Overview

This notebook performs analysis and visualization of geometric shapes from point data. It identifies shapes, calculates aspect ratios, fits geometric shapes like circles and rectangles, and uses clustering and Bézier curves for further analysis.

## Libraries Used

- `numpy`: For numerical operations.
- `matplotlib.pyplot`: For plotting data.
- `sklearn.cluster.DBSCAN`: For density-based clustering.
- `scipy.interpolate.splprep, splev`: For spline interpolation and Bézier curve fitting.
- `scipy.spatial.ConvexHull`: For computing convex hulls.

## Functions

- **`read_csv(csv_path)`**: Reads coordinates from a CSV file and organizes them by shape and segment.
- **`calculate_aspect_ratio(points)`**: Computes the aspect ratio of a convex hull surrounding the given points.
- **`calculate_perimeter(hull)`**: Calculates the perimeter of the convex hull.
- **`identify_shape(points)`**: Identifies the shape based on compactness, aspect ratio, and number of vertices.
- **`separate_shapes(fragments)`**: Separates points into outer and inner categories based on their proximity to the boundaries.
- **`fit_rectangle(points)`**: Calculates the bounding rectangle for a given set of points.
- **`fit_circle(points, num_points=100)`**: Fits a circle to the given points and generates circle points.
- **`fit_bezier_curve(points, num_points=100)`**: Fits a Bézier curve to the set of points using spline interpolation.
- **`filter_points_within_circle(points, center, radius)`**: Filters points that lie within a specified circle.

## Process

1. **Read CSV Files**: Load point data from CSV files using `read_csv()`.
2. **Separate Points**: Use `separate_shapes()` to categorize points into outer and inner regions.
3. **Fit Geometric Shapes**:
   - **Rectangle**: Fit a bounding rectangle to outer points using `fit_rectangle()`.
   - **Circle**: Fit a circle to inner points using `fit_circle()`.
4. **Filter Points**: Filter inner points that lie within the fitted circle using `filter_points_within_circle()`.
5. **Clustering**: Apply DBSCAN clustering to the filtered inner points within the circle.
6. **Fit Bézier Curves**: Fit Bézier curves to clusters of points using `fit_bezier_curve()`.
7. **Average Circle**: Compute an average circle based on Bézier curves and plot it.
8. **Visualization**: Plot the outer rectangle, inner circle, points, and fitting curves using `matplotlib`.

## Results and Visualization

- The plot shows:
  - The bounding rectangle for outer points (blue).
  - The fitted circle for inner points (red).
  - Bézier curves fitted to clustered inner points.
  - An average connecting circle (green).

- **Statistics Printed**:
  - Number of outer points.
  - Number of inner points.
  - Number of inner points within the fitted circle.
  - Average center and radius of the connecting circle.


# Video Demo Link
https://drive.google.com/drive/folders/1ayGKNKzwrGbwFgeNlyLk5egusN7Jt8Rj?usp=drive_link
