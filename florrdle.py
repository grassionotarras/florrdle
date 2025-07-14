import justpy as jp
import warnings
import random

warnings.filterwarnings("ignore")

w = [
    "air", "amulet", "ankh", "ant-egg", "antennae", "bandage", "basic",
    "basil", "battery", "beetle-egg", "blood-stinger", "blueberries", "bone",
    "bubble", "bur", "cactus", "card", "carrot", "claw", "clover", "cogwheel",
    "coin", "compass", "coral", "corn", "corruption", "cotton", "cutter",
    "dahlia", "dandelion", "dark-mark", "dice", "disc", "domino", "fang",
    "faster", "fragment", "glass", "golden-leaf", "grapes", "heavy", "honey",
    "iris", "jelly", "laser", "leaf", "light", "light-bulb", "lightning",
    "magic-bubble", "magic-cactus", "magic-cotton", "magic-eye",
    "magic-missile", "magic-stick", "magic-stinger", "magnet", "mana-orb",
    "mecha-antennae", "mecha-missile", "mimic", "missile", "mjolnir",
    "monstera", "moon-rock", "mysterious-powder", "mysterious-stick",
    "nazar-amulet", "orange", "pearl", "peas", "pharaoh's-crown", "pincer",
    "plank", "poker-chip", "pollen", "poo", "privet-berry", "rice", "rock",
    "root", "rose", "rubber", "salt", "sand", "shell", "shovel", "soil",
    "sponge", "square", "starfish", "talisman-of-evasion", "third-eye",
    "tomato", "triangle", "uranium", "wax", "web", "wing", "yggdrasil",
    "yin-yang", "yucca"
]
r = random.choice(w)


def Home():
    wp = jp.QuasarPage(tailwind=True)
    mdiv = jp.Div(a=wp, classes="h-screen bg-gray-200")
    
    div = jp.Div(a=mdiv,
                 text="Florrdle",
                 classes="text-3xl shadow bg-gray-100 px-2")
    
    inp = jp.Input(a=mdiv,
       placeholder="Your guess here...",
       classes="border border-blue-400 rounded m-2 h-8 w-40")

    btn = jp.Button(
        a=mdiv,
        text="Guess",
        classes="border-2 border-blue-400 rounded px-2 hover:border-blue-600 bg-blue-300 hover:bg-blue-400 text-white"
    )

    resdiv = jp.Div(a=mdiv,
           text="",
           classes="text-xl px-2")

    async def press(self, msg):
        user_input = inp.value.lower()
        res = []

        for i, char in enumerate(user_input):
            if i < len(r):
                if char == r[i]:
                    res.append(char.upper())
                elif char in r:
                    res.append(char.lower())
                else:
                    res.append("X")
            else:
                res.append("X")

        resdiv.text = "".join(res)

        if user_input == r:
            resdiv.text = "Correct!"

    
    btn.on('click', press)
    
    return wp

jp.Route("/", Home)
jp.justpy(Home, port=8000)