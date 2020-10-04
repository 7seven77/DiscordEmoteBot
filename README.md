# DiscordBot

## Setting up

The files `requirements.txt` and `Procfile` are used for deployment to Heroku. If you are not using Heroku, I don't think you need them.

`requirements.txt` contains the packages that Heroku will `pip install`, any new packages used should be added here

## Adding emotes

Created to be used in a similar way to Twitch emotes.
Channel emotes usually have a prefix related to the channel and popular emotes usually have variants named in the same fashion. That is the format this bot uses except for the fact that there is a space between the shared prefix and the rest of the word.
This shared prefix should be used as the directory name in the `images` directory and the images should be uploaded as `fullEmoteName.png`.

## Packages

- [discord.py](https://discordpy.readthedocs.io/en/latest/index.html)

- [python-dotenv](https://github.com/theskumar/python-dotenv)

- [Pillow](https://pillow.readthedocs.io/en/stable/)

## Important

When contributing to or using this repo, do not upload your ```.env``` file as this can leak sensitive information such as the bot's token

Using ```git update-index --skip-worktree .env``` should allow you to change the ```.env``` file locally and not have the changes be uploaded
