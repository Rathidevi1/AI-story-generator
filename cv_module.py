import random

def analyze_image(image):
    """
    Simulated object detection function.
    You can replace this with real CV models later.
    """
    simulated_objects = [
        "dog", "cat", "child", "tree", "book", "window",
        "bicycle", "cloud", "ball", "car", "bird", "flower","school","teacher","laptop"
    ]

    # Return 2 to 4 random objects
    detected = random.sample(simulated_objects, k=random.randint(2, 4))
    return detected
