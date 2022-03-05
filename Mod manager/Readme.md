## Mod manager
This is a mod manager to manage your mods and update them when there is an updated version uploaded somewhere.
By default it will check for updates every time you start firefox, but you can change this behaviour.

### Installation
These files should be copied directly to your chrome folder to start using it. You will see a QN extension button where your extensions usually are on the toolbar. Just press it and you will access the mod manager (you can move this button anywhere you want, just like you can do with regular extensions).

### Limitations
Right now the mod manager is not 100% finished. It's just a beta and it's likely that it will have some problems. Things like changing a mod requires firefox to be restarted for them to take effect once you activate them.

Another missing feature is a "panic shortcut" that could disable all mods as to avoid issues if someone installs a mod that somehow breaks the UI and then they can't access firefox UI anymore. 
If you have this problem, edit `Mods-loader.uc.js` and uncomment this line:
<pre>var dbDel = indexedDB.deleteDatabase("FirefoxMods");<pre>

That will delete the whole database, and then you will be able to restart operations.