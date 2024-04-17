module.exports = {
  // Specify the URL of your GitHub repository
  repositoryUrl: 'https://github.com/lukzimmermann/DigitecScrapy',

  // Optionally, you can specify other configuration options for Semantic Release
  branches: ['main'], // Specify which branches trigger releases
  plugins: [
    // List of Semantic Release plugins to use
    // Example plugins:
    '@semantic-release/commit-analyzer', // Analyzes commits to determine the release type
    '@semantic-release/release-notes-generator', // Generates release notes based on commits
    '@semantic-release/github', // Publishes releases to GitHub
    // Add more plugins as needed
  ],
};
