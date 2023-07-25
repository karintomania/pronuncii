const record = document.querySelector('#record');
const recordAgain = document.querySelector('#record-again');
const stop = document.querySelector('#stop');
const soundClips = document.querySelector('.sound-clips');
const recordingFile = document.querySelector('#id_recording');

//main block for doing the audio recording

if (navigator.mediaDevices.getUserMedia) {

  const constraints = { audio: true };
  let chunks = [];

  let onSuccess = function(stream) {
    const mediaRecorder = new MediaRecorder(stream);

    record.onclick = function() {
      mediaRecorder.start();

    }

    stop.onclick = function() {
      mediaRecorder.stop();
      // mediaRecorder.requestData();

    }

    mediaRecorder.onstop = function(e) {

      const clipName = "your recording"

      const clipContainer = document.createElement('article');
      const audio = document.createElement('audio');

      clipContainer.classList.add('clip');
      audio.setAttribute('controls', '');

      clipContainer.appendChild(audio);
      soundClips.appendChild(clipContainer);

      audio.controls = true;
      const blob = new Blob(chunks, { 'type' : 'audio/ogg; codecs=opus' });
      chunks = [];
      const audioURL = window.URL.createObjectURL(blob);
      audio.src = audioURL;

      let container = new DataTransfer();
      let file = new File([blob], "sound.wav",{type:"audio/wav"});
      container.items.add(file);
      recordingFile.files = container.files;

    }

    recordAgain.onclick = function(){
        document.querySelector(".clip").remove();
        record.click();
    }

    mediaRecorder.ondataavailable = function(e) {
      chunks.push(e.data);
    }
  }

  let onError = function(err) {
     console.log('The following error occured: ' + err);
  }

  navigator.mediaDevices.getUserMedia(constraints).then(onSuccess, onError);

} else {
   console.log('getUserMedia not supported on your browser!');
}


