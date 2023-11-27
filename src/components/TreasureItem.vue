<template>
    <div class="w-full bg-gray-200 px-3 py-1 rounded-sm flex flex-col">
        <div class="flex justify-between">
            {{treasure.name}}
            <div>
                <button for="cameraFileInput">
                    <span class="btn">Open camera</span>
                    <input id="cameraFileInput" 
                            type="file" 
                            accept="image/*" 
                            capture="environment"
                            class="invisible" />
                </button>
                <button @click="expanded = !expanded">{{expanded ? "-":"+"}}</button>
            </div>
        </div>
        <div name="details" v-if="expanded">
            {{ treasure.description }}
            {{ treasure.points }} Points {{ treasure.limit > 1 ? `each, limit ${treasure.limit}` : ""}}
        </div>
    </div>
  </template>
  
<script setup>
import {ref} from 'vue'
import {useTreasureStore} from '../stores/treasureStore'

const treasureStore = useTreasureStore();

const props = defineProps({treasure: Object})

const expanded = ref(false);




</script>