class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1  # Light source
        self.map[5][2] = -1  # Walls

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)


class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        width = len(grid)
        height = len(grid[0])
        self.adaptee.set_dim((height, width))
        lights = []
        obstacles = []
        for i in range(width):
            for j in range(height):
                if grid[i][j] == 1:
                    lights.append((j, i))
                elif grid[i][j] == -1:
                    obstacles.append((j, i))

        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)

        return self.adaptee.generate_lights()


if __name__ == "__main__":
    system = System()
    light = Light([0, 0])
    adapter = MappingAdapter(light)
    system.get_lightening(adapter)
