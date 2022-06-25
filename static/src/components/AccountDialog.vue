<template>
    <q-dialog
        v-model="account_d"
        transition-show="slide-down"
        transition-hide="slide-up"
        position="top"
    >
        <q-card style="min-width: 350px">
            <q-card-section>
                <div class="text-h6">What would you like to do?</div>
            </q-card-section>

            <q-card-section class="q-pt-none">
                <!-- {{ user_is_authenticated }} -->
                <div class="row justify-around" v-if="user_is_authenticated">
                    <q-btn
                        type="a"
                        :href="routes?.auth_routes?.profile_page"
                        color="primary"
                        icon="mdi-account-cog"
                        label="Manage Account"
                        no-caps
                    />
                    <q-btn
                        type="a"
                        :href="`/accounts/logout/${redirect_query}`"
                        color="negative"
                        icon="mdi-logout-variant"
                        outline
                        label="Sign Out"
                        no-caps
                    />
                </div>
                <div v-else class="row justify-around">
                    <!-- :href="`/login/auth/${redirect_query}`" -->
                    <q-btn
                        type="a"
                        :href="`/login/auth/${redirect_query}`"
                        color="primary"
                        outline
                        label="Sign In"
                    />
                    <q-btn
                        color="primary"
                        label="Sign Up"
                        type="a"
                        :href="`/signup/auth/${redirect_query}`"
                    />
                </div>
            </q-card-section>

            <!-- <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Cancel" v-close-popup />
          <q-btn flat label="Search" v-close-popup />
        </q-card-actions> -->
        </q-card>
    </q-dialog>
</template>

<script setup>
import { computed, inject, onBeforeMount, ref, watch, watchEffect } from "vue";
import generateAuthUrls from "../composables/generateAuthUrls";

const query = ref(window.location.search);
const queries = ref(new URLSearchParams(query.value));
const next_url = queries.value.get("next");

const account_d = ref(false);
const routes = ref(inject("routes"));

const user_is_authenticated = inject("user_is_authenticated");

const { generateLink, redirect_query } = generateAuthUrls();

watchEffect(async () => {
    await generateLink(routes, next_url);
    // console.log(redirect_query);
});

// console.log();
// console.log(user_is_authenticated);

const openAccountDia = () => (account_d.value = true);

defineExpose({
    openAccountDia,
});
</script>

<style>
</style>