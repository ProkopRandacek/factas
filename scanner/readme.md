Collects info about the worls and writes is into a json file  

triggered by `/exportmap`  
exports info `script-output/{surface name}.json  

colleced info:  
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
