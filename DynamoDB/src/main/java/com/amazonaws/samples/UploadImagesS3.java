package com.amazonaws.samples;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.CannedAccessControlList;
import com.amazonaws.services.s3.model.ObjectMetadata;
import com.amazonaws.services.s3.model.PutObjectRequest;
import com.amazonaws.util.IOUtils;
import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;

import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.MalformedURLException;
import java.net.URL;

public class UploadImagesS3 {

	public static void main(String[] args) throws IOException {
        Regions clientRegion = Regions.US_EAST_1;
        String bucketName = "s3868658-images";//e.g., sxxxxxxx-s3test
        
        File file = new File("a1.json");

        JsonParser parser = new JsonFactory().createParser(file);

        JsonNode rootNode = new ObjectMapper().readTree(parser);
        ArrayNode songs = (ArrayNode) rootNode.get("songs");
        
        for (JsonNode song : songs) {
	        try {
	            //This code expects that you have AWS credentials set up per:
	            // https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html
	            AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
	            		.withCredentials(new ProfileCredentialsProvider("default"))
	                    .withRegion(clientRegion)
	                    .build();
	            
	            ObjectMetadata metadata = new ObjectMetadata();
	            
	            InputStream stream = new URL(song.get("img_url").asText()).openStream();
	            byte[] contentBytes = IOUtils.toByteArray(stream);
	        	Long contentLength = Long.valueOf(contentBytes.length);
	        	InputStream streams = new ByteArrayInputStream(contentBytes); 
	        	
	            metadata.setContentLength(contentLength);	
			    metadata.setContentType("image/png");
			    metadata.addUserMetadata("title", song.get("title").asText());
	            
	//             Upload a text string as a new object.

	            s3Client.putObject(bucketName,song.get("title").asText() ,streams, metadata);
	             
	            System.out.println("File " + song.get("title").asText() + " was uploaded.");  
	            stream.close();
	        } catch (AmazonServiceException e) {
	            // The call was transmitted successfully, but Amazon S3 couldn't process 
	            // it, so it returned an error response.
	            e.printStackTrace();
	        } catch (SdkClientException e) {
	            // Amazon S3 couldn't be contacted for a response, or the client
	            // couldn't parse the response from Amazon S3.
	            e.printStackTrace();
	        }
        }
    }

}


