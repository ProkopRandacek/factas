Downloads factorio, generates the map and exports it into a json  

run `./scan`  
info is exported to `./nauvis.json`  

collected info:  
- water tiles position
- ore tiles positions and amounts

example output:  
```
{
	"water": [
	[x, y],
	[x, y],
	...
	]
	"resources": {
		"stone": [
		[x, y, a],
		[x, y, a],
		...
		]
		"iron-ore": [
		[x, y, a],
		[x, y, a],
		...
		]
		"copper-ore": [
		[x, y, a],
		[x, y, a],
		...
		]
		"crude-oil": [
		[x, y, a],
		[x, y, a],
		...
		]
		"coal": [
		[x, y, a],
		[x, y, a],
		...
		]
	}
}
```
