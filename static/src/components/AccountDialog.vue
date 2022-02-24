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
                        :href="`/logout/auth/?next=${redirect_url}`"
                        color="primary"
                        outline
                        label="Sign Out"
                    />
                </div>
                <div v-else class="row justify-around">
                    <q-btn
                        type="a"
                        :href="`/login/auth/?next=${redirect_url}`"
                        color="primary"
                        outline
                        label="Sign In"
                    />
                    <q-btn
                        color="primary"
                        label="Sign Up"
                        type="a"
                        :href="`/login/auth/?next=${redirect_url}`"
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
import { inject, ref } from "vue";

const account_d = ref(false);

const user_is_authenticated = inject("user_is_authenticated");

const redirect_url = window.location.pathname;
// console.log();
// console.log(user_is_authenticated);

const openAccountDia = () => (account_d.value = true);

defineExpose({
    openAccountDia,
});
</script>

<style>
</style>