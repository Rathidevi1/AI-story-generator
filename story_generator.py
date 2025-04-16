def generate_story(objects):
    """
    Generates a simple story using the detected objects.
    No LLMs or billing required.
    """
    if not objects:
        return "No recognizable objects were found."

    story = f"Once upon a time, there was a place where {objects[0]} was the most interesting thing around."
    
    if len(objects) > 1:
        for obj in objects[1:]:
            story += f" Nearby, a {obj} played an important role in the scene."

    story += " Together, they created a peaceful, memorable moment that told a quiet, beautiful story."

    return story
