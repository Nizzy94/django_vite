<template>
    <q-dialog
        v-model="openSelectNotifyDialog"
        transition-show="slide-down"
        transition-hide="slide-up"
    >
        <q-card style="min-width: 350px">
            <q-card-section>
                <div class="text-h6">Account is not selected.</div>
            </q-card-section>
            <q-separator spaced />

            <q-card-actions class="q-pt-md" align="around">
                <q-btn v-close-popup color="primary" label="Ok" />

                <!-- </div> -->
            </q-card-actions>
        </q-card>
    </q-dialog>
    <q-dialog
        v-model="openConfirmDialog"
        transition-show="slide-down"
        transition-hide="slide-up"
    >
        <q-card style="min-width: 350px">
            <form
                :action="routes?.auth_routes?.socialaccount_connections"
                method="post"
            >
                <q-card-section>
                    <div class="text-h6">
                        Are you sure you want to remove your
                        <strong>{{ selected_account.provider }}</strong>
                        account?
                    </div>
                    <!-- {{ selected_account }} -->
                    <input
                        name="account"
                        :value="selected_account.id"
                        type="radio"
                        checked
                        hidden
                    />
                    <input
                        name="csrfmiddlewaretoken"
                        type="hidden"
                        :value="$q.cookies.get('csrftoken')"
                    />
                </q-card-section>
                <q-separator spaced />

                <q-card-actions class="q-pt-md" align="around">
                    <!-- {{ user_is_authenticated }} -->

                    <!-- <div class="row justify-around"> -->
                    <!-- :href="`/login/auth/${redirect_query}`" -->
                    <q-btn
                        v-close-popup
                        color="primary"
                        outline
                        label="Cancel"
                    />
                    <q-btn
                        color="negative"
                        type="submit"
                        name="action_remove"
                        label="Remove"
                    />
                    <!-- </div> -->
                </q-card-actions>
            </form>
        </q-card>
    </q-dialog>
</template>

<script setup>
import { ref, toRefs } from "@vue/reactivity";

const props = defineProps({
    selected_account: {
        type: Object,
        required: true,
    },
    // openDialog: {
    //     type: Boolean,
    //     required: true,
    // },
    routes: {
        type: Object,
        required: true,
    },
});

const { selected_account, routes } = toRefs(props);

const openConfirmDialog = ref(false);
const openSelectNotifyDialog = ref(false);
// const selected_account = ref();

defineExpose({ openConfirmDialog, openSelectNotifyDialog });
</script>

<style>
</style>