import numpy as np

points = [(3,6), (10,12), (-3,5), (12,20), (1,5)]

def euclideanDistance(points):
    euclidean_distances = []
    
    # Bu döngüyle her noktadan bir sonraki noktaya olan mesafeyi hesaplıyoruz
    for i in range(1, len(points)):
        x1, y1 = points[i-1]
        x2, y2 = points[i]
        
        # Euclidean distance formülü
        distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        euclidean_distances.append(distance)
    
    # En kısa mesafeyi bulmak için
    min_distance = min(euclidean_distances)
    print("En kısa mesafe: ", min_distance)
    return min_distance

euclideanDistance(points)
