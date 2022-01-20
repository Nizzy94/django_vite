import { ref } from "vue"
// import store from "../store"

const drawerFunctionality = () => {

    const leftDrawerOpen = ref(false)
        // const leftDrawerOpen = computed(() => store.state.leftDrawerOpen)
        // const leftDrawerOpen = ref(store.state.leftDrawerOpen)

    const toggleLeftDrawer = () => {
        console.log(leftDrawerOpen.value)
        leftDrawerOpen.value = !leftDrawerOpen.value
            // store.state.leftDrawerOpen = leftDrawerOpen.value
        console.log(leftDrawerOpen.value)
    }
    return {
        leftDrawerOpen,
        toggleLeftDrawer
    }

}

export default drawerFunctionality