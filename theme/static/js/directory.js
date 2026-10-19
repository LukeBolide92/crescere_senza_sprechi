function filterCourses(query) {
  const items = document.querySelectorAll('.course-card');
  items.forEach(i => {
    const txt = i.textContent.toLowerCase();
    i.style.display = txt.indexOf(query.toLowerCase()) > -1 ? '' : 'none';
  });
}
console.log('directory.js ok');
