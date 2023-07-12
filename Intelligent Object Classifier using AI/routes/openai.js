const express = require("express");
const { OpenAIApi, Configuration } = require("openai");
const router = express.Router();

/**
 * Generates completion for the given input using the OpenAI API.
 * @param {string} input - The prompt input for generating completion.
 * @returns {string|boolean} - The generated completion or false if no completion is available.
 * @throws {Error} - If there is an error in the OpenAI API request.
 */

async function generateCompletion(input) {
  try {
    const prompt = input;
    const maxTokens = 500;
    const n = 1;

    const configuration = new Configuration({
      apiKey: process.env.OPEN_AI_KEY,
    });

    const openai = new OpenAIApi(configuration);
    const response = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: prompt,
      max_tokens: maxTokens,
      n: n,
    });

    const { choices } = response.data;
    if (choices && choices.length > 0) {
      const completion = choices[0].text.trim();
      return completion;
    } else {
      return false;
    }
  } catch (error) {
    console.error("OpenAI API request failed:", error);
    res.status(500).json({ error: "Failed to generate output" });
  }
}

router.post("/", async (req, res) => {
  try {
    const { objectName } = req.body;
    let response;

    if (objectName === "Not holding anything") {
      response = "You are not holding anything.";
    } else {
      let prompt;

      if (objectName === "Holding a clip") {
        prompt = `What can you do with a clothespin? //in the output please include the name of the object for example "You're holding a clothespin" in bold and in the next line followed by bullet points of what you can do with the object each in a new line`;
      } else if (objectName === 'Holding a tooth brush //in the output please include the name of the object for example "You"re holding a tooth brush" in bold and in the next line followed by bullet points of what you can do with the object each in a new line') {
        prompt = `What are the possible uses of a tooth brush?`;
      } else if (objectName === "An apple") {
        prompt = `Show me the nutritional values, possible uses, and country of origin of ${objectName}.`;
      } else {
        // Handle any other cases here
        response = "Holding nothing or no object present";
      }
      if (prompt) {
        response = await generateCompletion(prompt);
      } else {
        response = "Invalid object name.";
      }
    }

    res.json({ response });
  } catch (error) {
    console.error("Error:", error);
    res.status(500).json({ error: "An error occurred" });
  }
});

module.exports = { router };
