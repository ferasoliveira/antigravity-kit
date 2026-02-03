#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const args = process.argv.slice(2);
const command = args[0];

const sourceDir = path.join(__dirname, '..', '.agent');
const targetDir = path.join(process.cwd(), '.agent');

if (command === 'init') {
    console.log('🚀 Initializing Antigravity Kit...');

    if (fs.existsSync(targetDir)) {
        console.log('⚠️  .agent folder already exists.');
        // Simple check for --force could be added here
    }

    try {
        // Copy .agent folder
        // Using cp -r for simplicity in this script, or recursive fs copy
        // Since this runs on user machine, let's use a recursive copy function or shell command if available. 
        // Node.js fs.cpSync is available in Node 16.7+.

        if (fs.cpSync) {
            fs.cpSync(sourceDir, targetDir, { recursive: true });
        } else {
            // Fallback for older node or just shell out
            if (process.platform === 'win32') {
                execSync(`xcopy "${sourceDir}" "${targetDir}" /E /I /Y`);
            } else {
                execSync(`cp -r "${sourceDir}" "${targetDir}"`);
            }
        }

        console.log('✅ Antigravity Kit installed successfully!');
        console.log('📂 .agent folder created.');
        console.log('👉 Run /orchestrate or /brainstorm to start.');
    } catch (error) {
        console.error('❌ Error installing kit:', error);
        process.exit(1);
    }

} else {
    console.log('Usage: npx antigravity-kit init');
    console.log('Commands:');
    console.log('  init  Install .agent templates into current directory');
}
