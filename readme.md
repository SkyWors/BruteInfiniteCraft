# ⭐ BruteInfiniteCraft

BruteInfiniteCraft is a simple program that use [InfiniteCraft](https://neal.fun/infinite-craft)'s API to randomly generate and store items with recipe.

## 🔧 Installation

- BIC use MySQL database to store items and recipes,
- Execute ``sql/database.sql`` script to create the database.

## 🤚 Usage

Run ``python3 main.py`` in any terminal from root directory to start the program.

## ⚙️ Configuration

Change workerNumber variable to choose how many worker you want to dig the API.

## ❓ Explications

In terminal result:
- [+] mean that the item was not in the database,
- [*] mean that the item is a first discovery,
- [_] mean nothing new.
- [Ｘ] mean that nothing can be crafted from items
