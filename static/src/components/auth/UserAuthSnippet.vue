<template>
    <div id="snippet" v-if="user_is_authenticated">
        <p v-if="user?.username">
            <strong>Note:</strong> you are already logged in as
            <span class="text-primary">
                {{ user.username[0].toUpperCase()
                }}{{ user.username.slice(1) }} </span
            >.
        </p>
    </div>
</template>

<script setup>
import { inject, onBeforeMount, ref } from "@vue/runtime-core";
import getAuthUser from "../../composables/getAuthUser";

const user_is_authenticated = inject("user_is_authenticated");
const { callAuthUser } = getAuthUser();
const user = ref({});
onBeforeMount(async () => {
    if (user_is_authenticated) {
        user.value = await callAuthUser();
    }
});
</script>

<style>
</style>