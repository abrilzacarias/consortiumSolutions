document.addEventListener('DOMContentLoaded', function() {
  const sidebarBtn = document.querySelector(".toggle");
  const sidebar = document.querySelector("aside");

  sidebarBtn.addEventListener("click", () => {
    document.body.classList.toggle("active");
  });
});
