<template>
<header class="navbar">
  <SidebarButton @toggle-sidebar="$emit('toggle-sidebar')"/>
  <slot></slot>

    <!--   <img -->
    <!--     class="logo" -->
    <!--     v-if="$site.themeConfig.logo" -->
    <!--     :src="$withBase($site.themeConfig.logo)" -->
    <!--     :alt="$siteTitle" -->
    <!--   > -->
    <!--   <span -->
    <!--     class="site-name" -->
    <!--     v-if="$siteTitle" -->
    <!--     :class="{ 'can-hide': $site.themeConfig.logo }" -->
    <!--   >{{ $siteTitle }}</span> -->
    <!-- </router-link> -->

    <!-- <div class="links"> -->
    <!--   <AlgoliaSearchBox -->
    <!--     v-if="isAlgoliaSearch" -->
    <!--     :options="algolia" -->
    <!--   /> -->
    <!--   <SearchBox v-else-if="$site.themeConfig.search !== false"/> -->
    <!-- </div> -->
  <DarkmodeSwitch/>
  </header>
</template>

<script>
import SidebarButton from '../vuepress/components/SidebarButton.vue'
import DarkmodeSwitch from '../vuepress/global-components/DarkmodeSwitch.vue'
// import AlgoliaSearchBox from '@AlgoliaSearchBox'
// import SearchBox from './SearchBox.vue'
// import NavLinks from './NavLinks.vue'

export default {
  components: { SidebarButton, DarkmodeSwitch }, // NavLinks, SearchBox, AlgoliaSearchBox },

//   computed: {
//     algolia () {
//       return this.$themeLocaleConfig.algolia || this.$site.themeConfig.algolia || {}
//     },

//     isAlgoliaSearch () {
//       return this.algolia && this.algolia.apiKey && this.algolia.indexName
//     }
//   }
}
</script>

<style lang="stylus">

@import '../vuepress/styles/config.styl'

.navbar
  padding 0.7rem 1.5rem
  line-height $navbarHeight - 1.4rem
  position fixed // relative
  a, span, img
    display inline-block
  .logo
    height $navbarHeight - 1.4rem
    min-width $navbarHeight - 1.4rem
    margin-right 0.8rem
    vertical-align top
  .site-name
    font-size 1.3rem
    font-weight 600
    color var(--text-color)
    position relative
  .links
    font-size 0.9rem
    position absolute
    right 1.5rem
    top 0.7rem

@media (max-width: $MQMobile)
  .navbar
    padding-left 4rem
    .can-hide
      display none
  .sidebar-button
    display:block
</style>
