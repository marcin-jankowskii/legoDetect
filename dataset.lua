
myFPS = 8 --setting frames per second to 6 so that myFPS*cameraAngleIncrement 360
function onParadeStart()

   -- Session->Animation->OpenGL animation export->

    sf=ldc.subfile() --get the reference to the Idraw file which contains the parts list
    pieceCounter = 1 --counter sove through the list of pieces
    cameraLoopCounter = 1 --move through differnt camera view loops for each piece
    frameCounter = 0 --keep track of a frame count to increment the camera angles for each camera loop
   
    cameraAngleIncrement = 360/myFPS --setting to 60 so that myFPS above Is 6, so that myFPS cameraAngleIncrement 360
    unviewPosition=ldc.vector()
    unviewPosition:set(10000, 10000,10000) --plece posistion when hiding from camera
    viewPosition = ldc.vector()
    viewPosition:set(25,25,25) -- piece posistion when viewing with camera


   -- don't forget that animation length and FPS are set in registration function
    --setup initial camera state


    cam=ldc.view():getCamera()
    camPos=ldc.vector()
    camPos:set(50,-50,50) --canera posistion set to introduce variation In the viewing angle during camera rotation
    camDist = 1358  --camera distance set to accomodate large pieces
    cam:setThirdPerson(camPos, camDist, 0, 0, 0)
    cam:apply(0)

    --place all pieces out of view

    refCnt=sf:getRefCount()
    for i=1, refCnt do
        sf:getRef(i):setPos(unviewPosition)
    end
    sf:getRef(1):setPos(viewPosition)--put first plece in place
end   --end function onParadeStart()


function onParadeFrame()

    frameCounter = frameCounter + 1 --increment the frame counter for tracking purposes below 
    cam=ldc.view():getCamera()
    
    if cameraLoopCounter == 1 then --rotate the camera 360 degrees around the piece on the first axis
        cam:setThirdPerson(camPos, camDist, cameraAngleIncrement*frameCounter, 0, 0)
        cam:apply(0)
        if frameCounter == myFPS then --if finished a complete rotation of the camera, go on to the next step
            frameCounter = 0
            cameraLoopCounter = 2
        end
    elseif cameraLoopCounter == 2 then --rotate the camera 360 degrees around the piece on the second axis
        cam:setThirdPerson(camPos, camDist, 0, cameraAngleIncrement*frameCounter, 0)
        cam:apply(0)
        if frameCounter == myFPS then --if finished a complete rotation of the camera, go on to the next step
            frameCounter = 0
            cameraLoopCounter = 3
        end
    elseif cameraLoopCounter == 3 then 
        cam:setThirdPerson(camPos, camDist, 0, 0, cameraAngleIncrement*frameCounter)  --rotate the camera 360 degrees around the piece on the third axis
        cam:apply(0)
        if frameCounter == myFPS then -- if finished a complete rotation of the camera, go on to the next step
            frameCounter = 0
            cameraLoopCounter = 4
        end
    elseif cameraLoopCounter == 4 then --rotate the camera 360 degrees around the piece on two axis
        cam:setThirdPerson(camPos, camDist, 0, cameraAngleIncrement*frameCounter, cameraAngleIncrement*frameCounter)
        cam:apply(0)
        if frameCounter == myFPS then --if finished a complete rotation of the camera, go on to the next step
            frameCounter = 0
            cameraLoopCounter = 5
        end
    elseif cameraLoopCounter == 5 then --rotate the camera 360 degrees around the piece on two different axis
        cam:setThirdPerson(camPos, camDist, cameraAngleIncrement*frameCounter, cameraAngleIncrement*frameCounter, cameraAngleIncrement*frameCounter)
        cam:apply(0)
        if frameCounter == myFPS then --if finished a complete rotation of the camera, go back to the first step
            frameCounter = 0
            cameraLoopCounter = 1
            if pieceCounter == refCnt then --if there are no more pieces, go back to the beginning
                sf:getRef(pieceCounter):setPos(unviewPosition)
                pieceCounter = 1
                sf:getRef(pieceCounter):setPos(viewPosition)
                cam:setThirdPerson(camPos, camDist, 0, 0, 0)
                cam:apply(0)
            else --otherwise switch to the next piece
                sf:getRef(pieceCounter):setPos(unviewPosition)
                pieceCounter = pieceCounter + 1
                sf:getRef(pieceCounter):setPos(viewPosition) 
                cam:setThirdPerson(camPos, camDist, 0, 0, 0)
                cam:apply(0)
            end
        end
    end
end

function register()
    local ani = ldc.animation('Parade')
    ani:setLength(230)  
    ani:setFPS(8)        -- Ustaw FPS na 8, jak zdefiniowano na początku skryptu

    ani:setEvent('start', 'onParadeStart')
    ani:setEvent('frame', 'onParadeFrame')

end


register()