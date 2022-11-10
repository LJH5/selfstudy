<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import "./assets/css/index.scss"

export default {
  name: 'App'
}
</script>

<style>

</style>
