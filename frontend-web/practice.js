// Load saved notes from localStorage when the page loads
window.onload = function() {
    displaySavedNotes();
  };
  
  document.getElementById('save-btn').addEventListener('click', saveNote);
  
  function saveNote() {
    const title = document.getElementById('note-title').value.trim();
    const content = document.getElementById('note-content').value.trim();
  
    if (title && content) {
      const note = {
        title: title,
        content: content
      };
      saveToLocalStorage(note);
      displaySavedNotes();
  
      // Clear input fields
      document.getElementById('note-title').value = '';
      document.getElementById('note-content').value = '';
    } else {
      alert('Please enter both a title and content for the note.');
    }
  }
  
  function saveToLocalStorage(note) {
    let notes = JSON.parse(localStorage.getItem('notes')) || [];
    notes.push(note);
    localStorage.setItem('notes', JSON.stringify(notes));
  }
  
  function displaySavedNotes() {
    const savedNotesDiv = document.getElementById('saved-notes');
    savedNotesDiv.innerHTML = ''; // Clear existing notes
    const notes = JSON.parse(localStorage.getItem('notes')) || [];
  
    notes.forEach((note, index) => {
      const noteDiv = document.createElement('div');
      noteDiv.classList.add('note');
      noteDiv.innerHTML = `
        <h3>${note.title}</h3>
        <p>${note.content}</p>
      `;
      savedNotesDiv.appendChild(noteDiv);
    });
  }
  