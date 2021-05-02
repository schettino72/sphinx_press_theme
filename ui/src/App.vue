<script>
export default {
  name: 'App',
  data() {
    return {
      isSidebarOpen: false,
      swUpdateEvent: null
    };
  },
  computed: {
    pageClasses () {
      //const userPageClass = this.$page.frontmatter.pageClass
      return [
        {
         // 'no-navbar': !this.shouldShowNavbar,
          'sidebar-open': this.isSidebarOpen,
         // 'no-sidebar': !this.shouldShowSidebar
        },
       // userPageClass
      ]
    }
  },
  methods: {
    toggleSidebar (to) {
      this.isSidebarOpen = typeof to === 'boolean' ? to : !this.isSidebarOpen
    },
  },
}
</script>

<style>
</style>
