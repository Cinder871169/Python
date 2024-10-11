def tinh_dien_tich(x1, y1, x2, y2, x3, y3):
    """Calculate the area of a triangle given its vertices."""
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))


def is_point_in_triangle(px, py, x1, y1, x2, y2, x3, y3):
    """Check if a point is inside a triangle using the area method."""
    area = tinh_dien_tich(x1, y1, x2, y2, x3, y3)
    area1 = tinh_dien_tich(px, py, x2, y2, x3, y3)
    area2 = tinh_dien_tich(x1, y1, px, py, x3, y3)
    area3 = tinh_dien_tich(x1, y1, x2, y2, px, py)
    return area == area1 + area2 + area3


def add_active_intervals(active_intervals, new_interval):
    """Add new intervals to the list of active intervals."""
    active_intervals.append(new_interval)
    active_intervals.sort()  # Keep intervals sorted


def remove_active_intervals(active_intervals, remove_interval):
    """Remove intervals from the list of active intervals."""
    active_intervals.remove(remove_interval)


def calculate_covered_area(triangles):
    """Calculate the total area covered by triangles."""
    events = []
    for x1, y1, x2, y2, x3, y3 in triangles:
        # Create events for triangle edges
        events.append((x1, "start", (y1, y2, y3)))
        events.append((x2, "end", (y1, y2, y3)))

    # Sort events based on x-coordinates
    events.sort(key=lambda x: x[0])

    total_area = 0
    active_intervals = []
    last_x = events[0][0]

    for event in events:
        current_x = event[0]

        # Calculate total height covered by active intervals
        if active_intervals:
            height = calculate_total_height(active_intervals)
            total_area += height * (current_x - last_x)

        if event[1] == "start":
            add_active_intervals(active_intervals, event[2])
        else:
            remove_active_intervals(active_intervals, event[2])

        last_x = current_x

    return total_area


def calculate_total_height(active_intervals):
    """Calculate the total height covered by the active intervals."""
    y_coords = []
    for interval in active_intervals:
        y_coords.extend(interval)

    y_coords = sorted(set(y_coords))  # Get unique y-coordinates
    height = 0

    for i in range(1, len(y_coords)):
        height += max(0, y_coords[i] - y_coords[i - 1])  # Calculate covered height

    return height


# Input from the user
n = int(input("Enter number of triangles: "))  # Number of triangles
triangles = []

for _ in range(n):
    # Input six integers for each triangle
    triangles.append(list(map(int, input().split())))

# Calculate the total covered area
area = calculate_covered_area(triangles)
print(area)
