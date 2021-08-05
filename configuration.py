class Configuration:
    def __init__(self, screen_size, framerate, flags):
        # screen size
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.size = screen_size
        self.center = self.width / 2, self.height / 2

        self.framerate = framerate

        self.flags = flags
