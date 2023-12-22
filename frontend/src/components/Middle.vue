<template>
  <div class="middle">
    <main>
      <CorrectionPage v-if="page === 'CorrectionPage'"/>
      <IndexPage v-if="page === 'IndexPage'"/>
      <GlareOutPage v-if="page === 'GlareOutPage'"/>
    </main>
  </div>
</template>

<script>
import IndexPage from "@/components/page/IndexPage.vue";
import CorrectionPage from "@/components/page/CorrectionPage.vue";
import GlareOutPage from "@/components/page/GlareOutPage.vue";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Middle",
  data: function () {
    return {page: 'IndexPage', submitCycleId: undefined}
  },
  components: {
    GlareOutPage,
    CorrectionPage,
    IndexPage,
  },
  beforeCreate() {
    this.$root.$on("onChangePage", (page, kwargs = undefined) => {
      if (kwargs !== undefined) {
        for (const key in kwargs) {
          this[key] = kwargs[key];
        }
      }
      this.page = page;
    });
  }
}

</script>

<style scoped>
.middle {
  margin-top: 1rem;
  overflow: auto;
}

main {
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius);
  padding: 0.5rem;
}
</style>