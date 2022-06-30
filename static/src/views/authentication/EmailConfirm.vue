<template>
    <ProfileGeneral>
        <template #form_content="{ routes }">
            <div class="form_content">
                <div v-if="confirmation">
                    <p class="q-mb-md">
                        Please confirm that
                        <a :href="`mailto:${confirmation.email}`">{{
                            confirmation.email
                        }}</a>
                        is an e-mail address for user
                        <strong class="text-primary">{{
                            confirmation.user
                        }}</strong
                        >.
                    </p>

                    <!-- {{ routes?.auth_routes?.account_email }} -->

                    <form method="post" :action="currentRoute">
                        <CSRFToken />
                        <q-btn
                            type="submit"
                            label="Confirm"
                            color="secondary"
                            text-color="dark"
                        />
                    </form>
                </div>
                <div v-else>
                    <p>
                        This e-mail confirmation link expired or is invalid.
                        Please
                        <a :href="routes?.auth_routes?.account_email">
                            issue a new e-mail confirmation request </a
                        >.
                    </p>
                </div>
            </div>
        </template>
    </ProfileGeneral>
</template>

<script setup>
import { inject } from "@vue/runtime-core";
import ProfileGeneral from "../../components/auth/ProfileGeneral.vue";
import CSRFToken from "../../components/CSRFToken.vue";
const confirmation = inject("confirmation");
const currentRoute = window.location.href;
</script>

<style>
</style>