import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()
 
mc.postToChat("Whack it")

pos = mc.player.getTilePos()
mc.postToChat(pos)

mc.setBlocks(pos.x -1, pos.y, pos.z+3, pos.x +1, pos.y+2, pos.z +3, block.STONE.id)

mc.postToChat("Get Ready")
time.sleep(4)
mc.postToChat("Go")

blockslit = 0
points = 0

while blockslit < 9:
    time.sleep(0.2)
    blockslit = blockslit + 1
    lightCreated = False
    while not lightCreated:
        xpos = pos.x + random.randint(-1, 1)
        ypos = pos.y + random.randint(0, 2)
        zpos = pos.z + 3
        if mc.getBlock(xpos, ypos,zpos) == block.STONE.id:
            mc.setBlock(xpos, ypos, zpos, block.GLOWSTONE_BLOCK.id)
            lightCreated = True
            
    for hitBlock in mc.events.pollBlockHits():
        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.GLOWSTONE_BLOCK.id:
            mc.setBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z, block.STONE.id)
            blockslit = blockslit - 1
            points = points + 1
            
mc.postToChat("Game Over" + str(points))