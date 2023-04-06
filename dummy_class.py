class DummyModelForHuggingFace():
    def __init__(self) -> None:
        pass

    def push_to_hub(self, repo_name):
        print("Pushing to hub!!")



class DummyModelForLightning():
    def __init__(self, name):
        self.name = name
        self.model = DummyModelForHuggingFace()

    @staticmethod
    def load_from_checkpoint(checkpoint_path):
        return DummyModelForLightning("dummy")
    
    