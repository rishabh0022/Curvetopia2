import csv
import xml.etree.ElementTree as ET
import os

svg_file_path = os.path.expanduser('~/Test Dataset folder/input.svg')
csv_file_path = os.path.expanduser('~/Model/output.csv')

def parse_svg(svg_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()
    return root

def extract_paths(root):
    paths = []
    for elem in root.findall('.//{http://www.w3.org/2000/svg}path'):
        paths.append(elem.attrib['d'])
    return paths

def extract_circles(root):
    circles = []
    for elem in root.findall('.//{http://www.w3.org/2000/svg}circle'):
        cx = float(elem.attrib['cx'])
        cy = float(elem.attrib['cy'])
        circles.append((cx, cy))
    return circles

def extract_rects(root):
    rects = []
    for elem in root.findall('.//{http://www.w3.org/2000/svg}rect'):
        x = float(elem.attrib['x'])
        y = float(elem.attrib['y'])
        width = float(elem.attrib['width'])
        height = float(elem.attrib['height'])
        rects.append((x, y))
        rects.append((x + width, y))
        rects.append((x, y + height))
        rects.append((x + width, y + height))
    return rects


root = parse_svg(svg_file_path)

paths = extract_paths(root)
circles = extract_circles(root)
rects = extract_rects(root)


all_coordinates = []
all_coordinates.extend(circles)
all_coordinates.extend(rects)

with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y'])  # CSV header
    writer.writerows(all_coordinates)

print(f"Coordinates extracted and saved to {csv_file_path}")
