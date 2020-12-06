local function has_value(tab, val)
    for index, value in ipairs(tab) do
        if value == val then
            return true
        end
    end
    return false
end

# there is no need to actually create json. maybe just writting numbers separated by newlines and spaces would save some bytes and probably speed up python imput parse

script.on_nth_tick(3, function(NthTickEvent)
	local surface = game.get_surface("nauvis")
	local result = "{ \"water\": [ "

	-- tiles
	local existingTiles = {}
	local tiles = surface.find_tiles_filtered{}
	for index, tile in pairs(tiles) do
		if tile.name == "water" then
			result = result .. string.format("\n[%s,%s],", tile.position.x, tile.position.y)
		end
	end
	result = result:sub(1, -2)
	result = result .. " ], \"resources\": { "

	-- ores
	helpTable = {}
	local existingEntities = {}
	local entities = surface.find_entities_filtered{}
	for index, entity in pairs(entities) do
		if entity.type == "resource" then
			if not has_value(existingEntities, entity.name) then
				helpTable[entity.name] = {}
				table.insert(existingEntities, entity.name)
			end
			table.insert(helpTable[entity.name], string.format("\n[%s,%s,%s],", entity.position.x, entity.position.y, entity.amount))
		end
	end
	result = result:sub(1, -2)
	for k, _ in pairs(helpTable) do
		result = result .. string.format("\n\"%s\": [\n", k)
		for _, value in pairs(helpTable[k]) do
			result = result .. value
		end
		result = result:sub(1, -2)
		result = result .. "],"
	end
	result = result:sub(1, -2)
	result = result .. " } } "

	game.write_file(surface.name ..".json", result)
	game.print("done")
end)
