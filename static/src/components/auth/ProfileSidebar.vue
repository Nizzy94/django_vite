<template>
    <!-- {{ routes }} -->
    <div class="sidebar-list">
        <q-list bordered separator>
            <q-item
                clickable
                v-ripple
                tag="a"
                v-if="routes?.auth_routes?.profile_page"
                :class="{
                    'sidebar-list-item-active':
                        currentRoute == routes?.auth_routes?.profile_page,
                }"
                :href="routes?.auth_routes?.profile_page"
            >
                <q-item-section avatar>
                    <q-icon name="mdi-account" />
                </q-item-section>
                <q-item-section>
                    <q-item-label>Profile</q-item-label>
                </q-item-section>
            </q-item>

            <q-item
                clickable
                v-ripple
                tag="a"
                v-if="routes?.auth_routes?.account_email"
                :class="{
                    'sidebar-list-item-active':
                        currentRoute == routes?.auth_routes?.account_email,
                }"
                :href="routes?.auth_routes?.account_email"
            >
                <q-item-section avatar>
                    <q-icon name="mdi-email-open" />
                </q-item-section>
                <q-item-section>
                    <q-item-label>E-mails</q-item-label>
                </q-item-section>
            </q-item>

            <q-item
                clickable
                v-ripple
                v-if="routes?.auth_routes?.account_change_password"
                :class="{
                    'sidebar-list-item-active':
                        currentRoute ==
                        routes?.auth_routes?.account_change_password,
                }"
                :href="routes?.auth_routes?.account_change_password"
            >
                <q-item-section avatar>
                    <q-icon name="mdi-lock-reset" />
                </q-item-section>
                <q-item-section>
                    <q-item-label>Change Password</q-item-label>
                </q-item-section>
            </q-item>

            <q-item clickable v-ripple>
                <q-item-section avatar>
                    <q-icon name="mdi-google" />
                </q-item-section>
                <q-item-section>
                    <q-item-label>Social Accounts</q-item-label>
                </q-item-section>
            </q-item>
        </q-list>
    </div>
</template>

<script setup>
import { inject, ref } from "@vue/runtime-core";

// console.log(inject("routes"));
const routes = inject("routes");
const currentRoute = ref(window.location.href);
</script>

<style lang="sass">
.sidebar-list
    width: 100%

    @media (min-width: $breakpoint-md-min)
        width: 70%

.sidebar-list-item-active
    background-color: $primary !important
    color: white !important
    font-weight: bold !important
</style>