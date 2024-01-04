Lims Discord Bot

Lims is a Discord bot built using the discord.py library, providing various utility commands and fun interactions. The bot has features like anime and manga search, as well as SFW (Safe for Work) commands such as hug, pat, slap, and more.
Project Structure

    bot.py: The main Python script containing the Discord bot implementation.
    requirements.txt: File containing the required Python libraries.
    README.md: Documentation file for the project.

Dependencies

    discord.py: Library for interacting with the Discord API.
    askitsu: A wrapper for the Kitsu API to search for anime and manga information.
    requests: Library for making HTTP requests.

Usage

    Install dependencies by running:

    bash

pip install -r requirements.txt

Set up a Discord bot on the Discord Developer Portal.

Replace the placeholder in client.run("") with your Discord bot token.

Run the bot:

bash

    python bot.py

    Invite the bot to your Discord server and use various commands such as !help, !anime, !manga, and more.

Discord Commands

    !ping: Check the bot's latency.
    !help: Display the help menu with available commands.
    !anime <anime name>: Search for information about an anime.
    !manga <manga name>: Search for information about a manga.
    !hug <user>: Hug a mentioned user.
    !pat <user>: Pat a mentioned user.
    !neko: Get a random neko image.
    !kiss <user>: Kiss a mentioned user.
    And more...

Important Note

    The provided bot.py script is a basic example and can be extended with additional features.
    Ensure that the bot has the necessary permissions to read messages, send messages, and embed links in the channels where it operates.

Feel free to customize and enhance this project based on your preferences and requirements!
