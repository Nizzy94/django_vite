<template>
    <q-layout view="hHh lpR lFf">
        <CustomHeader />
        <q-page-container>
            <q-page style="max-width: 1440px" class="q-mx-auto">
                <slot name="page_content" />
            </q-page>
        </q-page-container>
        <CustomFooter />
    </q-layout>
</template>

<script>
import { computed, ref } from "@vue/reactivity";
import CustomHeader from "./Header.vue";
import CustomFooter from "./Footer.vue";

import getUrls from "../../composables/getUrls";
import { onBeforeUnmount, provide } from "@vue/runtime-core";
import { useQuasar } from "quasar";

export default {
    name: "Base",
    components: {
        CustomHeader,
        CustomFooter,
    },
    setup() {
        const name = ref("my name");
        const $q = useQuasar();

        const { routes, callUrls } = getUrls();

        // onMounted(async () => {

        callUrls();

        console.log(routes);

        if (routes.value) {
            provide(
                "routes",
                computed(() => routes.value)
            );
        }

        // console.log($sizes.xl)
        onBeforeUnmount(() => {
            $q.loading.show({
                spinner: "QSpinnerPie",
            });
        });

        // })

        return { name, routes };
    },
};
</script>

<style>
@charset "UTF-8";
/* #base {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
