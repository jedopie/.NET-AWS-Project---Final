// Copyright 2012-2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.

package com.amazonaws.samples;

import java.io.File;
import java.util.Iterator;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.client.builder.AwsClientBuilder;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;

public class MusicLoadData {

    public static void main(String[] args) throws Exception {

        AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard()
        	.withRegion(Regions.US_EAST_1)
            .withCredentials(new ProfileCredentialsProvider("default"))
            .build();

        DynamoDB dynamoDB = new DynamoDB(client);

        Table table = dynamoDB.getTable("music");
        
        File file = new File("a1.json");

        JsonParser parser = new JsonFactory().createParser(file);

        JsonNode rootNode = new ObjectMapper().readTree(parser);
        ArrayNode songs = (ArrayNode) rootNode.get("songs");
        System.out.println(songs.size());

        for (int i = 0; i < songs.size(); i++) {          

            String title = songs.get(i).get("title").asText();
            String artist = songs.get(i).get("artist").asText();
            int year = songs.get(i).get("year").asInt();
            String web_url = songs.get(i).get("web_url").asText();
            String image_url = songs.get(i).get("img_url").asText();

            try {
                table.putItem(new Item()
                		.withPrimaryKey("title", title, "year", year)
                		.withString("artist", artist)
                		.withString("web_url", web_url)
                		.withString("image_url",image_url));
                System.out.println("PutItem succeeded: " + artist + " " + year + ": " + title + " " + i);

            }
            catch (Exception e) {
                System.err.println("Unable to add movie: " + artist + " " + year);
                System.err.println(e.getMessage());
                break;
            }
        }
        parser.close();
    }
}