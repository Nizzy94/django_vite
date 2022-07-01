<template>
    <ProfileGeneral>
        <template #form_content="{ routes }">
            <div v-if="process == 'connect'">
                <div class="text-h5 q-mb-md">Connect {{ provider }}</div>
                <p>
                    You are about to connect a new third party account from
                    {{ provider }}.
                </p>
            </div>
            <div v-else>
                <div class="text-h5 q-mb-md">Sign In with {{ provider }}</div>
                <p>
                    You are about to sign in using a third party account from
                    {{ provider }}.
                </p>
            </div>
            <div>
                <form method="post">
                    <CSRFToken />
                    <q-btn
                        label="Continue"
                        type="submit"
                        color="secondary"
                        text-color="dark"
                    />
                </form>
            </div>
        </template>
    </ProfileGeneral>
</template>

<script setup>
import { inject } from "@vue/runtime-core";
import { Cookies } from "quasar";
import ProfileGeneral from "../../components/auth/ProfileGeneral.vue";
import getQueries from "../../composables/getQueries";
import CSRFToken from "../../components/CSRFToken.vue";

const { getQueryValue } = getQueries();
const process = getQueryValue("process");
const provider = inject("provider");
// console.log(provider);
</script>

<style>
</style>