<template>
    <ProfileGeneral>
        <template #form_content="{ routes }">
            <p class="q-mb-md">Are you sure you want to sign out?</p>
            <form method="post" :action="routes?.auth_routes?.account_logout">
                <CSRFToken />

                <input
                    type="hidden"
                    v-if="redirect_field.value != 'None'"
                    :name="redirect_field.name"
                    :value="redirect_field.value"
                />

                <q-btn label="Sign Out" color="negative" type="submit" />
            </form>
        </template>
    </ProfileGeneral>
</template>

<script setup>
import CSRFToken from "../../components/CSRFToken.vue";
import ProfileGeneral from "../../components/auth/ProfileGeneral.vue";
import { inject } from "@vue/runtime-core";

const redirect_field = inject("redirect_field");
</script>

<style>
</style>