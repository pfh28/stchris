<template>
    <div class="w-full bg-gray-200 px-3 py-1 rounded-sm flex flex-col">
        <div class="flex justify-between">
            {{treasure.name}}
            <div class="flex flex-row flex-none space-x-1">
                <img class="w-8 h-8 flex-none rounded-lg" :src="answerImage"/>
                <cameraButton @fileAdded="processFile"/>
                <button class="w-8 h-8 flex-none bg-gray-400 rounded-lg grid place-content-center"
                 @click="expanded = !expanded">
                    <ChevronUpIcon class="w-5" v-if="expanded"/>
                    <ChevronDownIcon class="w-5" v-else=""/>
                </button>
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
import CameraButton from './CameraButton.vue'
import { ChevronUpIcon, ChevronDownIcon } from '@heroicons/vue/24/outline';

const treasureStore = useTreasureStore();

const props = defineProps({treasure: Object})

const expanded = ref(false);

const answerImage = ref("")

function processFile(fileList) {
    console.log(props.treasure.name)
    answerImage.value = window.URL.createObjectURL(fileList[0])
}


</script>