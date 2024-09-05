document.addEventListener("DOMContentLoaded", () => {
  const navbar = document.getElementById("navbar");
  const sidebar = document.getElementById("sidebar");
  const btnSidebarToggler = document.getElementById("btnSidebarToggler");
  const navClosed = document.getElementById("navClosed");
  const navOpen = document.getElementById("navOpen");

  btnSidebarToggler.addEventListener("click", (e) => {
      e.preventDefault();
      sidebar.classList.toggle("show");
      navClosed.classList.toggle("hidden");
      navOpen.classList.toggle("hidden");
  });

  sidebar.style.top = parseInt(navbar.clientHeight) - 1 + "px";
});

//{% block content %}
//{% endblock %}
//