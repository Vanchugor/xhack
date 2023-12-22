<template>
  <header>
    <nav>
      <ul>
        <li><a href="#" @click.prevent="changePage('IndexPage')">Главная</a></li>
        <li><a href="#" @click.prevent="changePage('CorrectionPage')">Цветокоррекция</a></li>
        <li><a href="#" @click.prevent="changePage('GlareOutPage')">Обезбличивание</a></li>
        <li><a href="https://github.com/Vanchugor/xhack">Ссылка на гит</a></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Header",
  methods: {
    changePage: function (page) {
      this.$root.$emit("onChangePage", page);
    }
  }
}
</script>

<style scoped>
header {
  position: relative;
}

header .enter-or-register-box {
  float: top;
  text-align: right;
}

header nav {
  float: bottom;
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius);
  padding: 0.75rem 0.25rem;
  margin-top: 1rem;
}

header nav ul {
  margin: 0;
  padding: 0;
}

header nav ul li {
  display: inline;
  margin-left: 1rem;
}

header nav ul li::before {
  content: " | ";
  color: var(--border-color);
  margin-right: 1rem;
}

header nav ul li:first-child::before {
  content: " ";
  margin-right: 1rem;
}

header nav ul li a {
  text-decoration: none;
  color: var(--black-color);
  font-family: "Arial Narrow", sans-serif;
  font-weight: bold;
  text-transform: uppercase;
}
</style>