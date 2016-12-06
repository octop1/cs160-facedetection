# CV Web Interface

## Installing

Install the required modules:

`$ npm install`

## Running

Create + initialize Postgres:

`$ server-sh-scripts/startpsql.sh`

`$ server-sh-scripts/createdb.sh`

Initialize the server:

`$ node Server-dan.js`

>Initializing server...

> Live at Port 3000

>

> 160-pipeline>

Ta-da! Now navigate your browser to `127.0.0.1:3000`.

### Example use case:
- Open new job panel by pressing the + button.
- Select video file, OpenCV/OpenFace implementation, press "Queue Job".
- Video file will be uploaded to `/uploads`, job info will be sent to server. Once file is fully uploaded, job will be added to job list.
- Press "Start Job" to begin job. Page will send `start-job` POST request with job number to server.
- Server will call `execute()` on Job instance, `execute()` iterates through pipeline steps and executes shell code/applications for each respective step.

## To do

### Must do:

- Handle job creation:
  - [x] Implement file sanitation on server-side
    - [x] Check file mimetype on server-side
  - [ ] Store job info into Postgres

- [ ] Store and load user queues to/from database

- Handle job initialization:
  - [x] Call script which continues pipeline: (see Node.js [child_process](https://nodejs.org/api/child_process.html) docs for details on this)
      - FFMPEG for frame splitting
      - Process frames via OpenFace
      - Draw OpenCV implementation
      - Recombine frames with FFMPEG
      - [ ] Handle errors, exceptions for each
  - [ ] Serve finished video back to web interface
  - [ ] Remove temp files

- [ ] Assemble Passport.js/OpenID authentication implementation with this web interface

### Should do (code cleanup):

- [ ] Finish commenting jquery-test.js, rename it to something proper
- [ ] Convert status text changes and job processing icon show/hides (client-side) into separate functions ( setStatus(statusText), jobIconVisibility(true/false) )
- [ ] Convert jobStatus integers (server-side) into pseudo-enums
- [x] Rewrite Job queueing jQuery actions to load templated HTML instead of injecting HTML block snippets (use .parent to find proper job num, use jQuery .load())
- [ ] Re-write Job.js to be a class
- [ ] Have interface load what jobs are in current user's queue list on page load
- [x] Large files take time to upload. Unfortunately, the client-side automatically adds the job to the UI list before it knows if the file is uploaded, possibly causing errors. I'll need to modify the templated HTML to have the button disabled by default, and have a loop on the client-side to ping the server periodically if the job file is uploaded. Once the server begins processing the file (app.post('/create-job'...) ), the server will return that request with a truthy value, indicating the file is fully uploaded.

### Want to do:

- [ ] Implement progress bar in web interface for each pipeline step
- [ ] ~~Support FBX file output from tracked face animation~~
  - ~~Support files: [rigged face](http://www.turbosquid.com/FullPreview/Index.cfm/ID/341150)~~


# OpenFace notes

`$ bin/FaceLandmarkVid -device 0`

Webcam drops tons of frames, then kinda works, then crashes (see openface_crash.txt) - Justin
