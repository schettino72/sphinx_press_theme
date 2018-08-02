<template>
  <div class="sidebar">
    <slot></slot>
    <!-- <slot name="top"/> -->
    <!-- <ul class="sidebar-links" v-if="items.length"> -->
    <!--   <li v-for="(item, i) in items" :key="i"> -->
    <!--     <SidebarGroup -->
    <!--       v-if="item.type === 'group'" -->
    <!--       :item="item" -->
    <!--       :first="i === 0" -->
    <!--       :open="i === openGroupIndex" -->
    <!--       :collapsable="item.collapsable" -->
    <!--       @toggle="toggleGroup(i)" -->
    <!--     /> -->
    <!--     <SidebarLink v-else :item="item"/> -->
    <!--   </li> -->
    <!-- </ul> -->
    <!-- <slot name="bottom"/> -->
  </div>
</template>

<script>
//import SidebarGroup from './SidebarGroup.vue'
//import SidebarLink from './SidebarLink.vue'
//import { isActive } from './vuepress/util'

export default {
  /*
  components: { SidebarGroup, SidebarLink },

  props: ['items'],

  data () {
    return {
      openGroupIndex: 0
    }
  },

  created () {
    this.refreshIndex()
  },

  watch: {
    '$route' () {
      this.refreshIndex()
    }
  },

  methods: {
    refreshIndex () {
      const index = resolveOpenGroupIndex(
        this.$route,
        this.items
      )
      if (index > -1) {
        this.openGroupIndex = index
      }
    },

    toggleGroup (index) {
      this.openGroupIndex = index === this.openGroupIndex ? -1 : index
    },

    isActive (page) {
      return isActive(this.$route, page.path)
    }
  }
}

function resolveOpenGroupIndex (route, items) {
  for (let i = 0; i < items.length; i++) {
    const item = items[i]
    if (item.type === 'group' && item.children.some(c => isActive(route, c.path))) {
      return i
    }
  }
  return -1
*/
}
</script>

<style lang="stylus">
@import './vuepress/styles/config.styl'

.sidebar
  ul
    padding 0
    margin 0
    list-style-type none
  a
    display inline-block
  .nav-links
    display none
    border-bottom 1px solid $borderColor
    padding 0.5rem 0 0.75rem 0
    a
      font-weight 600
    .nav-item, .repo-link
      display block
      line-height 1.25rem
      font-size 1.1em
      padding 0.5rem 0 0.5rem 1.5rem
  .sidebar-links
    padding 1.5rem 0

@media (max-width: $MQMobile)
  .sidebar
    .nav-links
      display block
      .dropdown-wrapper .nav-dropdown .dropdown-item a.router-link-active::after
        top calc(1rem - 2px)
    .sidebar-links
      padding 1rem 0

/********************/

/* rename some classes as no control on what comes from sphinx:
  - sidebar-heading => caption
  - sidebar-link => reference
  - sidebar-sub-headers => toctree-l2
    Note: sidebar-sub-headers refers to ul in Vuepress
          while toctree-l2 referes to li in sphinx
  - active => current
*/

/**** SidebarGroup.vue  ***/
.sidebar-group
  &:not(.first)
    margin-top 1em
  .sidebar-group
    padding-left 0.5em
  &:not(.collapsable)
    .caption
      cursor auto
      color inherit

.caption
  color #999
  transition color .15s ease
  cursor pointer
  font-size 1.1em
  font-weight bold
  // text-transform uppercase
  padding 0 1.5rem
  margin-top 0
  margin-bottom 0.5rem
  &.open, &:hover
    color inherit
  .arrow
    position relative
    top -0.12em
    left 0.5em
  &:.open .arrow
    top -0.18em

.sidebar-group-items /* FIXME sphinx toc equivalent */
  transition height .1s ease-out
  overflow hidden

/**** end: SidebarGroup.vue  ***/

/**** SidebarLink.vue  ***/
/*.sidebar .sidebar-sub-headers*/
.sidebar .toctree-l1 ul
  padding-left 1rem
  font-size 0.95em

/* extra indication of current, since no support to hight current location */
.toctree-l1.current > ul
   border-left: .2rem solid #6fd9a7

.sidebar a.reference
  font-weight 400
  display inline-block
  color $textColor
  border-left 0.25rem solid transparent
  padding 0.35rem 1rem 0.35rem 1.25rem
  line-height 1.4
  width: 100%
  box-sizing: border-box
  &:hover
    color $accentColor
  &.current
    font-weight 600
    color $accentColor
    border-left-color $accentColor
  .sidebar-group &
    padding-left 2rem
  .toctree-l2 &
    padding-top 0.25rem
    padding-bottom 0.25rem
    border-left none
    &.current
      font-weight 500

/**** end: SidebarLink.vue  ***/


</style>
