# ⭐ BruteInfiniteCraft

BruteInfiniteCraft is a simple program that use [InfiniteCraft](https://neal.fun/infinite-craft)'s API to randomly generate and store items with recipe.

![image](https://github.com/SkyWors/BruteInfiniteCraft/assets/70440695/29f791a0-5d5e-49e0-a1d2-282230345927)

## 🔧 Installation

- BIC use MySQL database to store items and recipes,
- Execute ``sql/database.sql`` script to create the database,
- Rename ``.env.example`` to ``.env`` and fill database credentials.

## 🤚 Usage

Run ``python3 main.py`` in any terminal from root directory to start the program.

## ⚙️ Configuration

Change workerNumber variable to choose how many worker you want to dig the API.

## ❓ Explications

In terminal result:
- [+] mean that the item was not in the database,
- [*] mean that the item is a first discovery,
- [ｘ] mean that nothing can be crafted from items
- [_] mean just a new recipe.
