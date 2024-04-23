<! --Template for the Navigation >
<template>
  <div id="app">
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/plant_list">Plants List</router-link></li>
      </ul>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>


export default {
  name: 'App',
}
</script>

<style scoped>
/* Styles for the navigation bar */

body, html {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  height: 100%;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

nav {
  background-color: #333;
  padding: 10px;
  text-align: right;
}

nav ul {
  list-style-type: none;
  padding: 0;
}

nav ul li {
  display: inline;
}

nav ul li router-link {
  color: white;
  text-decoration: none;
  padding: 8px 16px;
}

nav ul li router-link.active {
  background-color: #555;
}
</style>
