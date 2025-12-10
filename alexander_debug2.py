from logic.logic_api import logicAPI
from alexander_debug import SpectatorUI


def main():
    logic = logicAPI()
    spec_ui = SpectatorUI()
    spec_ui.run()


if __name__ == "__main__":
    main()
