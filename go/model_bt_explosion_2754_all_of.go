/*
 * Onshape REST API
 *
 * The Onshape REST API consumed by all clients.
 *
 * API version: 1.111
 * Contact: api-support@onshape.zendesk.com
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// BtExplosion2754AllOf struct for BtExplosion2754AllOf
type BtExplosion2754AllOf struct {
	StartingPositionId BtMicroversionIdAndConfiguration2338 `json:"startingPositionId,omitempty"`
	ExplodeSteps []BtExplosionStepFeature3008 `json:"explodeSteps,omitempty"`
	BtType string `json:"btType,omitempty"`
}
